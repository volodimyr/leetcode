from search import WordDictionary

def test_example_from_problem():
    """Test the exact example from the problem statement"""
    wd = WordDictionary()
    
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    
    assert wd.search("pad") == False, "Should not find 'pad'"
    assert wd.search("bad") == True, "Should find 'bad'"
    assert wd.search(".ad") == True, "Should match '.ad' with 'bad', 'dad', 'mad'"
    assert wd.search("b..") == True, "Should match 'b..' with 'bad'"
    
    print("[PASS] Problem example test passed")


def test_empty_dictionary():
    """Test operations on empty dictionary"""
    wd = WordDictionary()
    
    assert wd.search("test") == False, "Empty dictionary should not find any word"
    assert wd.search(".") == False, "Empty dictionary should not match single dot"
    assert wd.search("...") == False, "Empty dictionary should not match dots"
    
    print("[PASS] Empty dictionary test passed")


def test_exact_match():
    """Test exact word matching without wildcards"""
    wd = WordDictionary()
    
    wd.addWord("hello")
    wd.addWord("world")
    
    assert wd.search("hello") == True, "Should find 'hello'"
    assert wd.search("world") == True, "Should find 'world'"
    assert wd.search("hell") == False, "Should not find 'hell'"
    assert wd.search("worlds") == False, "Should not find 'worlds'"
    
    print("[PASS] Exact match test passed")


def test_single_wildcard():
    """Test patterns with single wildcard"""
    wd = WordDictionary()
    
    wd.addWord("cat")
    wd.addWord("bat")
    wd.addWord("rat")
    
    assert wd.search(".at") == True, "Should match '.at'"
    assert wd.search("c.t") == True, "Should match 'c.t'"
    assert wd.search("ca.") == True, "Should match 'ca.'"
    assert wd.search(".a.") == True, "Should match '.a.'"
    
    print("[PASS] Single wildcard test passed")


def test_multiple_wildcards():
    """Test patterns with multiple wildcards"""
    wd = WordDictionary()
    
    wd.addWord("abc")
    wd.addWord("xyz")
    
    assert wd.search("...") == True, "Should match '...' with 'abc' or 'xyz'"
    assert wd.search("a..") == True, "Should match 'a..' with 'abc'"
    assert wd.search(".b.") == True, "Should match '.b.' with 'abc'"
    assert wd.search("..c") == True, "Should match '..c' with 'abc'"
    assert wd.search("..d") == False, "Should not match '..d'"
    
    print("[PASS] Multiple wildcards test passed")


def test_all_wildcards():
    """Test pattern with all wildcards"""
    wd = WordDictionary()
    
    wd.addWord("test")
    
    assert wd.search("....") == True, "Should match '....' with 'test'"
    assert wd.search(".....") == False, "Should not match '.....' (length mismatch)"
    assert wd.search("...") == False, "Should not match '...' (length mismatch)"
    
    print("[PASS] All wildcards test passed")


def test_single_character():
    """Test single character words"""
    wd = WordDictionary()
    
    wd.addWord("a")
    wd.addWord("b")
    
    assert wd.search("a") == True, "Should find 'a'"
    assert wd.search("b") == True, "Should find 'b'"
    assert wd.search(".") == True, "Should match '.' with 'a' or 'b'"
    assert wd.search("c") == False, "Should not find 'c'"
    
    print("[PASS] Single character test passed")


def test_overlapping_words():
    """Test words with common prefixes"""
    wd = WordDictionary()
    
    wd.addWord("car")
    wd.addWord("card")
    wd.addWord("care")
    wd.addWord("careful")
    
    assert wd.search("car") == True, "Should find 'car'"
    assert wd.search("card") == True, "Should find 'card'"
    assert wd.search("car.") == True, "Should match 'car.' with 'card' or 'care'"
    assert wd.search("car..") == False, "Should not match 'car..' (length mismatch with card/care)"
    assert wd.search("car....") == True, "Should match 'car....' with 'careful'"
    
    print("[PASS] Overlapping words test passed")


def test_wildcard_beginning():
    """Test wildcard at the beginning"""
    wd = WordDictionary()
    
    wd.addWord("apple")
    wd.addWord("apply")
    
    assert wd.search(".pple") == True, "Should match '.pple' with 'apple'"
    assert wd.search(".pply") == True, "Should match '.pply' with 'apply'"
    assert wd.search(".pp..") == True, "Should match '.pp..' with both words"
    
    print("[PASS] Wildcard beginning test passed")


def test_wildcard_end():
    """Test wildcard at the end"""
    wd = WordDictionary()
    
    wd.addWord("test")
    wd.addWord("text")
    
    assert wd.search("tes.") == True, "Should match 'tes.' with 'test'"
    assert wd.search("tex.") == True, "Should match 'tex.' with 'text'"
    assert wd.search("te..") == True, "Should match 'te..' with both words"
    
    print("[PASS] Wildcard end test passed")


def test_no_match():
    """Test patterns that should not match"""
    wd = WordDictionary()
    
    wd.addWord("hello")
    
    assert wd.search("world") == False, "Should not find 'world'"
    assert wd.search("h.....") == False, "Should not match 'h....' (length mismatch)"
    assert wd.search("x....") == False, "Should not match 'x....' (wrong prefix)"
    assert wd.search(".ello") == True, "Should match '.ello' with 'hello'"
    assert wd.search(".ellx") == False, "Should not match '.ellx'"
    
    print("[PASS] No match test passed")


def test_duplicate_words():
    """Test adding duplicate words"""
    wd = WordDictionary()
    
    wd.addWord("test")
    wd.addWord("test")
    wd.addWord("test")
    
    assert wd.search("test") == True, "Should find 'test' after multiple additions"
    assert wd.search("....") == True, "Should match '....' with 'test'"
    
    print("[PASS] Duplicate words test passed")


def test_long_words():
    """Test with longer words"""
    wd = WordDictionary()
    
    long_word = "abcdefghij"
    wd.addWord(long_word)
    
    assert wd.search(long_word) == True, "Should find long word"
    assert wd.search("abcdefghi.") == True, "Should match with wildcard at end"
    assert wd.search(".bcdefghij") == True, "Should match with wildcard at beginning"
    assert wd.search("abcd.fghij") == True, "Should match with wildcard in middle"
    
    print("[PASS] Long words test passed")


def test_wildcard_no_alternatives():
    """Test wildcard when there are no alternatives"""
    wd = WordDictionary()
    
    wd.addWord("aaa")
    
    assert wd.search(".aa") == True, "Should match '.aa' with 'aaa'"
    assert wd.search("a.a") == True, "Should match 'a.a' with 'aaa'"
    assert wd.search("aa.") == True, "Should match 'aa.' with 'aaa'"
    assert wd.search("...") == True, "Should match '...' with 'aaa'"
    
    print("[PASS] Wildcard no alternatives test passed")


def test_different_lengths():
    """Test words of different lengths"""
    wd = WordDictionary()
    
    wd.addWord("a")
    wd.addWord("ab")
    wd.addWord("abc")
    wd.addWord("abcd")
    
    assert wd.search(".") == True, "Should match '.' with 'a'"
    assert wd.search("..") == True, "Should match '..' with 'ab'"
    assert wd.search("...") == True, "Should match '...' with 'abc'"
    assert wd.search("....") == True, "Should match '....' with 'abcd'"
    assert wd.search(".....") == False, "Should not match '.....' (no word that long)"
    
    print("[PASS] Different lengths test passed")


def test_complex_patterns():
    """Test complex wildcard patterns"""
    wd = WordDictionary()
    
    wd.addWord("at")
    wd.addWord("and")
    wd.addWord("an")
    wd.addWord("add")
    
    assert wd.search("a") == False, "Should not match 'a'"
    assert wd.search(".at") == False, "Should not match '.at' (length mismatch)"
    assert wd.search("an.") == True, "Should match 'an.' with 'and'"
    assert wd.search(".nd") == True, "Should match '.nd' with 'and'"
    assert wd.search("a.d") == True, "Should match 'a.d' with 'and' or 'add'"
    assert wd.search("a.") == True, "Should match 'a.' with 'at' or 'an'"
    assert wd.search(".") == False, "Should not match '.' (no single char words except none exist)"
    
    print("[PASS] Complex patterns test passed")


def run_all_tests():
    """Run all test cases"""
    print("Running WordDictionary tests...\n")
    
    test_example_from_problem()
    test_empty_dictionary()
    test_exact_match()
    test_single_wildcard()
    test_multiple_wildcards()
    test_all_wildcards()
    test_single_character()
    test_overlapping_words()
    test_wildcard_beginning()
    test_wildcard_end()
    test_no_match()
    test_duplicate_words()
    test_long_words()
    test_wildcard_no_alternatives()
    test_different_lengths()
    test_complex_patterns()
    
    print("\n" + "="*50)
    print("All tests passed! [PASS]")
    print("="*50)


if __name__ == "__main__":
    run_all_tests()