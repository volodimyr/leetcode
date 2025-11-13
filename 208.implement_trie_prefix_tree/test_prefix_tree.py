from prefix_tree import Trie


def test_basic_operations():
    """Test basic insert, search, and startsWith operations"""
    trie = Trie()
    
    # Insert and search
    trie.insert("apple")
    assert trie.search("apple") == True, "Should find 'apple'"
    assert trie.search("app") == False, "Should not find 'app' as complete word"
    assert trie.startsWith("app") == True, "Should find 'app' as prefix"
    
    # Insert another word
    trie.insert("app")
    assert trie.search("app") == True, "Should find 'app' after insertion"
    
    print("✓ Basic operations test passed")


def test_empty_trie():
    """Test operations on empty trie"""
    trie = Trie()
    
    assert trie.search("test") == False, "Empty trie should not find any word"
    assert trie.startsWith("test") == False, "Empty trie should not find any prefix"
    
    print("✓ Empty trie test passed")


def test_single_character():
    """Test single character words"""
    trie = Trie()
    
    trie.insert("a")
    assert trie.search("a") == True, "Should find single character 'a'"
    assert trie.search("ab") == False, "Should not find 'ab'"
    assert trie.startsWith("a") == True, "Should find 'a' as prefix"
    
    print("✓ Single character test passed")


def test_overlapping_words():
    """Test words that overlap/share prefixes"""
    trie = Trie()
    
    words = ["car", "card", "care", "careful", "cat", "cats"]
    for word in words:
        trie.insert(word)
    
    # Search for all inserted words
    for word in words:
        assert trie.search(word) == True, f"Should find '{word}'"
    
    # Test prefixes
    assert trie.startsWith("car") == True, "Should find 'car' as prefix"
    assert trie.startsWith("ca") == True, "Should find 'ca' as prefix"
    assert trie.startsWith("c") == True, "Should find 'c' as prefix"
    
    # Test non-existent words
    assert trie.search("cards") == False, "Should not find 'cards'"
    assert trie.search("ca") == False, "Should not find 'ca' as complete word"
    
    print("✓ Overlapping words test passed")


def test_prefix_vs_word():
    """Test distinction between prefix and complete word"""
    trie = Trie()
    
    trie.insert("hello")
    
    # "hell" is a prefix but not a word
    assert trie.startsWith("hell") == True, "Should find 'hell' as prefix"
    assert trie.search("hell") == False, "Should not find 'hell' as complete word"
    
    # Now insert "hell" as a word
    trie.insert("hell")
    assert trie.search("hell") == True, "Should find 'hell' as complete word"
    assert trie.search("hello") == True, "Should still find 'hello'"
    
    print("✓ Prefix vs word test passed")


def test_duplicate_insertions():
    """Test inserting the same word multiple times"""
    trie = Trie()
    
    trie.insert("test")
    trie.insert("test")
    trie.insert("test")
    
    assert trie.search("test") == True, "Should find 'test' after multiple insertions"
    
    print("✓ Duplicate insertions test passed")


def test_long_words():
    """Test with longer words"""
    trie = Trie()
    
    long_word = "abcdefghijklmnopqrstuvwxyz"
    trie.insert(long_word)
    
    assert trie.search(long_word) == True, "Should find long word"
    assert trie.startsWith("abcdef") == True, "Should find prefix of long word"
    assert trie.search("abcdef") == False, "Should not find partial word"
    
    print("✓ Long words test passed")


def test_similar_words():
    """Test words that differ by only one character"""
    trie = Trie()
    
    trie.insert("bat")
    trie.insert("cat")
    trie.insert("rat")
    
    assert trie.search("bat") == True, "Should find 'bat'"
    assert trie.search("cat") == True, "Should find 'cat'"
    assert trie.search("rat") == True, "Should find 'rat'"
    assert trie.search("hat") == False, "Should not find 'hat'"
    
    print("✓ Similar words test passed")


def test_example_from_problem():
    """Test the exact example from the problem statement"""
    trie = Trie()
    
    trie.insert("apple")
    assert trie.search("apple") == True, "Expected True"
    assert trie.search("app") == False, "Expected False"
    assert trie.startsWith("app") == True, "Expected True"
    trie.insert("app")
    assert trie.search("app") == True, "Expected True"
    
    print("✓ Problem example test passed")


def test_chain_of_words():
    """Test inserting words that form a chain"""
    trie = Trie()
    
    words = ["a", "ab", "abc", "abcd", "abcde"]
    for word in words:
        trie.insert(word)
    
    for word in words:
        assert trie.search(word) == True, f"Should find '{word}'"
        assert trie.startsWith(word) == True, f"Should find '{word}' as prefix"
    
    assert trie.search("abcdef") == False, "Should not find 'abcdef'"
    assert trie.startsWith("abcdef") == False, "Should not find 'abcdef' as prefix"
    
    print("✓ Chain of words test passed")


def test_no_common_prefix():
    """Test words with no common prefixes"""
    trie = Trie()
    
    words = ["apple", "banana", "cherry", "date"]
    for word in words:
        trie.insert(word)
    
    for word in words:
        assert trie.search(word) == True, f"Should find '{word}'"
    
    assert trie.search("apricot") == False, "Should not find 'apricot'"
    
    print("✓ No common prefix test passed")


def run_all_tests():
    """Run all test cases"""
    print("Running Trie tests...\n")
    
    test_basic_operations()
    test_empty_trie()
    test_single_character()
    test_overlapping_words()
    test_prefix_vs_word()
    test_duplicate_insertions()
    test_long_words()
    test_similar_words()
    test_example_from_problem()
    test_chain_of_words()
    test_no_common_prefix()
    
    print("\n" + "="*50)
    print("All tests passed! ✓")
    print("="*50)


if __name__ == "__main__":
    run_all_tests()