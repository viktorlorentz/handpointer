from handpointer import pointer

p= pointer.pointer()
print('Raise your hand into view to control the pointer. Touch thumb and index finger to activate the pointer')

while True:
    print('Pointer position:', p.get())
