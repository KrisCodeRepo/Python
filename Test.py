#def strStr(self, haystack: str, needle: str) -> int:
haystack = "hello"
needle = "ll"

try:
    index = haystack.index(needle)
    print(f"Substring found at index {index}")
except ValueError:
    print("Substring not found")

smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)