import re
from WordToNumberRussian.extractor import NumberExtractor
from patterns import pattern_repl_dict

with open("mod_ukrf") as zakon:
    ukrf_text = zakon.read()

ukrf_text_mod = ukrf_text
for pattern, repl in pattern_repl_dict.items():
    ukrf_text_mod = re.sub(pattern, repl, ukrf_text_mod, flags=re.IGNORECASE)

# words to numbers
# extractor = NumberExtractor()
# ukrf_text_mod = extractor.replace_groups(ukrf_text_mod, with_separators=True)


with open("mod_ukrf", mode="w") as file:
    file.write(ukrf_text_mod)