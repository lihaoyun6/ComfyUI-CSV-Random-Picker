import random
import time

class CSVRandomPicker:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "csv_string": ("STRING", {
                    "multiline": True,
                    "default": "apple,banana,cat,dog"
                }),
                "count": ("INT", {
                    "default": 1,
                    "min": 1,
                    "max": 1000
                }),
                "separator": ("STRING", {
                    "default": ","
                }),
                "seed": ("INT", {
                    "default": 0,
                    "min": 0,
                    "max": 1125899906842624
                }),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "pick_random_items"
    CATEGORY = "Custom/Utils"

    @classmethod
    def IS_CHANGED(cls, *args, **kwargs):
        return True

    def pick_random_items(self, csv_string, count, separator, seed):
        items = [item.strip() for item in csv_string.split(separator) if item.strip()]
        if not items:
            return ("",)

        actual_count = min(count, len(items))

        rng = random.Random()
        rng.seed(seed)

        selected_items = rng.sample(items, actual_count)
        result = separator.join(selected_items)
        return (result,)

NODE_CLASS_MAPPINGS = {
    "CSVRandomPicker": CSVRandomPicker
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CSVRandomPicker": "CSV Random Picker"
}