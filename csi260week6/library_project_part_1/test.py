from library_item import LibraryItem

li = LibraryItem("shadows upon time",
                 "42069",
                 ["romance", "sci-fi"])

print("Name: ",li.name)
print("ISBN", li.isbn)
print("Tags: ", li.tags)

print(li.match("romance"))
print(li.match("fantasy"))
print(li.match("sci-fi"))


print(li.to_short_string())