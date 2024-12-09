import check50
import check50.c

@check50.check()
def exists():
    """degrees.py exists."""
    check50.exists("degrees.py")

@check50.check(exists)
def compiles():
    """degrees.py compiles."""
    check50.c.compile("degrees.py")

@check50.check(compiles)
def encrypts_a_as_b():
    """encrypts "a" as "b" using 1 as key"""
    check50.run("./degrees 1").stdin("a").stdout("ciphertext:\s*b\n", "ciphertext: b\n").exit(0)

@check50.check(compiles)
def encrypts_barfoo_as_yxocll():
    """encrypts "barfoo" as "yxocll" using 23 as key"""
    check50.run("./degrees 23").stdin("barfoo").stdout("ciphertext:\s*yxocll\n", "ciphertext: yxocll\n").exit(0)

@check50.check(compiles)
def encrypts_BARFOO_as_EDUIRR():
    """encrypts "BARFOO" as "EDUIRR" using 3 as key"""
    check50.run("./degrees 3").stdin("BARFOO").stdout("ciphertext:\s*EDUIRR\n", "ciphertext: EDUIRR\n").exit(0)

@check50.check(compiles)
def encrypts_BaRFoo_FeVJss():
    """encrypts "BaRFoo" as "FeVJss" using 4 as key"""
    check50.run("./degrees 4").stdin("BaRFoo").stdout("ciphertext:\s*FeVJss\n", "ciphertext: FeVJss\n").exit(0)

@check50.check(compiles)
def encrypts_barfoo_as_onesbb():
    """encrypts "barfoo" as "onesbb" using 65 as key"""
    check50.run("./degrees 65").stdin("barfoo").stdout("ciphertext:\s*onesbb\n", "ciphertext: onesbb\n").exit(0)

@check50.check(compiles)
def checks_for_handling_non_alpha():
    """encrypts "world, say hello!" as "iadxp, emk tqxxa!" using 12 as key"""
    check50.run("./degrees 12").stdin("world, say hello!").stdout("ciphertext:\s*iadxp, emk tqxxa!\n", "ciphertext: iadxp, emk tqxxa!\n").exit(0)

@check50.check(compiles)
def handles_no_argv():
    """handles lack of argv[1]"""
    check50.run("degrees").exit(1)
