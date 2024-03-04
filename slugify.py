import unicodedata
import re

class slugify:
    def run(self, value, allow_unicode=False):
        """
        Taken from https://github.com/django/django/blob/master/django/utils/text.py
        Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
        dashes to single dashes. Remove characters that aren't alphanumerics,
        underscores, or hyphens. Convert to lowercase. Also strip leading and
        trailing whitespace, dashes, and underscores.
        """
        #print(f'Before: {value}')
        value = str(value).replace("%20", " ")
        if allow_unicode:
            value = unicodedata.normalize("NFKC", value)
        else:
            value = (
                unicodedata.normalize("NFKD", value)
                .encode("ascii", "ignore")
                .decode("ascii")
            )
        value = re.sub(r"[^\w,.#\s-]", " ", value)
        value = value.replace("  ", " ")
        #print(f'After: {value}')
        return value.strip()
        # return re.sub(r'[-\s]+', '-', value).strip('-_')
        