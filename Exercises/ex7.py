#!/usr/local/bin/python
# _*_ coding: utf-8 _*_
# More Printing

print("Mary had a ")
print("little lamb " * 3)
print("Its fleece was white as %s." % 'snow')
print("And everywhere that Mary went.")
print("." * 10)  # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# Python adds space if used comma while joining strings.
# Use + instead for good formatting.
print(end1, end2, end3, end4, end5, end6)

print(end7 + " " + end8 + " " + end9 + " " + end10 + " " + end11 + " " + end12)

print("sa" + "chin", "is", 5 + 25, "years",
      "old. {0}".format("Multiple formatting do works."))

print("Reverse order {5} {4} {3} {2} {1} {0} "
      .format(end7, end8, end9, end10, end11, end12))
