from cats import minimum_mewtations, furry_fixes, autocorrect, lines_from_file
import os
os.chdir(os.path.dirname(__file__))
all_words = lines_from_file("data/words.txt")
common_words = lines_from_file("data/common_words.txt")
minimum_mewtations.call_count = 0
print(autocorrect("woll", common_words, minimum_mewtations, 4))
print(minimum_mewtations.call_count)    # minimum_mewtations should be memoized
minimum_mewtations.call_count = 0
print(autocorrect("woll", common_words, furry_fixes, 4))
print(minimum_mewtations.call_count)
minimum_mewtations.call_count = 0
print(autocorrect("woll", common_words, minimum_mewtations, 4)) # identical to the first call
print(minimum_mewtations.call_count)