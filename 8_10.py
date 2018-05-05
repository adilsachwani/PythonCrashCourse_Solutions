def show_magicians(magician_names):
    for magician_name in magician_names:
        print(magician_name.title())

def make_great(magician_names):
    for i,magician_name in enumerate(magician_names):
        magician_names[i] = "The Great " + magician_name


magicians = ['adil aslam','naveed raza','saba zafar','rija asif butt','amna habibi']

show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)