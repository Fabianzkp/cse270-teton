import pytest
import json
from build_sentences import (
    get_seven_letter_word,
    parse_json_from_file,
    choose_sentence_structure,
    get_pronoun,
    get_article,
    fix_agreement,
    get_word,
    build_sentence,
    pronouns,
    structures,
)

# Test get_seven_letter_word
def test_get_seven_letter_word(mocker):
    mocker.patch("builtins.input", return_value="perfect")
    result = get_seven_letter_word()
    assert result == "PERFECT"
    assert len(result) == 7

def test_get_seven_letter_word_too_short(mocker):
    mocker.patch("builtins.input", return_value="short")
    with pytest.raises(ValueError):
        get_seven_letter_word()

# Test parse_json_from_file
def test_parse_json_from_file(tmp_path):
    test_data = {"nouns": ["cat"], "verbs": ["run"]}
    file_path = tmp_path / "test.json"
    with open(file_path, "w") as f:
        json.dump(test_data, f)
    result = parse_json_from_file(file_path)
    assert result == test_data

def test_parse_json_from_file_not_found():
    with pytest.raises(FileNotFoundError):
        parse_json_from_file("nonexistent.json")

def test_parse_json_from_file_invalid_json(tmp_path):
    file_path = tmp_path / "invalid.json"
    with open(file_path, "w") as f:
        f.write("not json")
    with pytest.raises(json.JSONDecodeError):
        parse_json_from_file(file_path)

# Test choose_sentence_structure
def test_choose_sentence_structure(mocker):
    mock_choice = mocker.patch("random.choice", return_value=structures[0])
    result = choose_sentence_structure()
    assert result == structures[0]
    mock_choice.assert_called_once_with(structures)

# Test get_pronoun
def test_get_pronoun(mocker):
    mock_choice = mocker.patch("random.choice", return_value="he")
    result = get_pronoun()
    assert result == "he"
    mock_choice.assert_called_once_with(pronouns)

# Test get_article
def test_get_article(mocker):
    mock_choice = mocker.patch("random.choice", return_value="a")
    result = get_article()
    assert result == "a"
    mock_choice.assert_called_once_with(["a", "the"])

# Test fix_agreement
def test_fix_agreement_he_she():
    sentence = ["he", "quickly", "run", "to", "a", "small", "cat"]
    fix_agreement(sentence)
    assert sentence[2] == "runs"

def test_fix_agreement_article_a_to_an():
    sentence = ["a", "quickly", "apple", "runs", "to", "the", "cat"]
    fix_agreement(sentence)
    assert sentence[0] == "an"

def test_fix_agreement_the_start():
    sentence = ["the", "quickly", "cat", "to", "run", "on", "a", "small", "hill"]
    fix_agreement(sentence)
    assert sentence[4] == "runs"

def test_fix_agreement_no_change():
    sentence = ["they", "quickly", "run", "to", "a", "small", "cat"]
    fix_agreement(sentence)
    assert sentence[2] == "run"

# Test get_word
def test_get_word():
    assert get_word("A", ["cat", "dog"]) == "cat"  
    assert get_word("B", ["run", "jump"]) == "jump"  

# Test build_sentence
def test_build_sentence(mocker):
    mocker.patch("build_sentences.choose_sentence_structure", return_value=structures[0])
    mocker.patch("build_sentences.get_article", return_value="a")
    mocker.patch("build_sentences.get_pronoun", return_value="he")
    mocker.patch("build_sentences.get_word", side_effect=["small", "cat", "quickly", "run", "on", "big", "hill"])
    mocker.patch("build_sentences.parse_json_from_file", return_value={
        "adjectives": ["small"], "nouns": ["cat"], "adverbs": ["quickly"], "verbs": ["run"], "prepositions": ["on"]
    })
    sentence = build_sentence("ABCDEFG", structures[0], {
        "adjectives": ["small"], "nouns": ["cat"], "adverbs": ["quickly"], "verbs": ["run"], "prepositions": ["on"]
    })
    assert sentence == "A small cat quickly run on a big hill"  