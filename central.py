import assistent as asist


__help = ["help", "помощь", "h", "п"]
__charlistPath = ""
__charlistName = ""


while True:
    __input_str = input(f"[help]> ").lower()

    if __input_str in __help:
        __temp = "\t cl \t \t \t \t open a charlist. if not exists, make new. \n"
        __temp += "\t i make \t \t \t make new [inventory].\n"
        __temp += "\t i input \t \t \t input new item to [inventory].\n"
        __temp += "\t i edit \t \t \t edit item in [inventory].\n"
        __temp += "\t pool make \t \t \t make new [pool].\n"
        __temp += "\t pool input \t \t \t input new item to [pool].\n"
        __temp += "\t pool edit \t \t \t edit item in [pool].\n"
        __temp += "\t mb input \t \t \t input new item to magic book.\n"
        __temp += "\t mb edit \t \t \t edit item in magic book.\n"
        __temp += "\t bio edit \t \t \t edit item in bio.\n"
        __temp += "\n"
        __temp += "\t i o \t \t \t out [inventory].\n"
        __temp += "\t pool o \t \t out [pool].\n"
        __temp += "\t mb o \t \t \t out magic book.\n"
        __temp += " \t cl o \t \t \t out existing [charlist]. \n"
        __temp += "\n"
        __temp += " \t coming soon \t \t \t see planned features. \n"

        print(__temp)

    elif __input_str == "cl":
        __temp = "Open a charlist. Make new if not exisits. Charlist сontains a "
        __temp += "biography, inventory, pools, a book of magic. When a new "
        __temp += "Charlist is created, the creation of a biography will be triggered.. \n"
        __temp += " \t [path] -- path to core charlist file \n"
        __temp += " \t [filename] -- name of core charlist file \n"
        print(__temp)
        __charlistPath = input("[path]> ")
        if __charlistPath == "":
            __charlistPath = "files/"
        __charlistName = input("[filename]> ")
        __charlist = asist.CharList(__charlistPath,__charlistName)

    elif __input_str == "i make":
        __charlist = asist.CharList(__charlistPath,__charlistName)
        __temp = ""
        __temp += " \t [filename] -- name of inventory \n"
        print(__temp)
        __charlist.create_inventory(input("[filename]> "))

    elif __input_str == "i input":
        __charlist = asist.CharList(__charlistPath,__charlistName)
        __temp = ""
        __temp += " \t [filename] -- name of inventory \n"
        print(__temp)
        __charlist.input_inventory(input("[filename]> "))

    elif __input_str == "i edit":
        __charlist = asist.CharList(__charlistPath,__charlistName)
        __temp = ""
        __temp += " \t [filename] -- name of inventory \n"
        print(__temp)
        __charlist.edit_inventory(input("[filename]> "))

    elif __input_str == "pool make":
        __charlist = asist.CharList(__charlistPath,__charlistName)
        __temp = ""
        __temp += " \t [filename] -- name of pool \n"
        print(__temp)
        __charlist.create_pool(input("[filename]> "))

    elif __input_str == "pool input":
        __charlist = asist.CharList(__charlistPath,__charlistName)
        __temp = ""
        __temp += " \t [filename] -- name of pool \n"
        print(__temp)
        __charlist.input_pool(input("[filename]> "))

    elif __input_str == "pool edit":
        __charlist = asist.CharList(__charlistPath,__charlistName)
        __temp = ""
        __temp += " \t [filename] -- name of pool \n"
        print(__temp)
        __charlist.edit_pool(input("[filename]> "))

    elif __input_str == "mb input":
        __charlist = asist.CharList(__charlistPath,__charlistName)
        __charlist.input_inventory("spell_book")

    elif __input_str == "mb edit":
        __charlist = asist.CharList(__charlistPath,__charlistName)
        __charlist.edit_inventory("spell_book")

    elif __input_str == "bio edit":
        __charlist = asist.CharList(__charlistPath,__charlistName)
        __charlist.edit_bio()

    elif __input_str == "i o":
        __key = int(input("[access key (0-3)]>"))
        __charlist = asist.CharList(__charlistPath,__charlistName)
        print(__temp)
        __charlist.out_inventory(input("[filename]> "), __key)

    elif __input_str == "pool o":
        __charlist = asist.CharList(__charlistPath,__charlistName)
        __key = int(input("[access key (0-3)]>"))
        __temp = ""
        __temp += " \t [filename] -- name of inventory \n"
        print(__temp)
        __charlist.out_pool(input("[filename]> "), __key)

    elif __input_str == "mb o":
        __key = int(input("[access key (0-3)]>"))
        __charlist = asist.CharList(__charlistPath,__charlistName)
        __charlist.out_inventory("spell_book", __key)

    elif __input_str == "bio o":
        __charlist = asist.CharList(__charlistPath,__charlistName)
        __charlist.out_bio()

    elif __input_str == "cl o":
        __key = int(input("[access key (0-3)]>"))
        __charlist = asist.CharList(__charlistPath,__charlistName)
        __charlist.out(__key)

    elif __input_str == "coming soon":
        __temp = " \t \"generate\" feachures for biography, inventory and pools. \n"
        __temp += "\n"
        # __temp += "\"generate\" will randomly build a new catalog from "
        # __temp += "resources. The \"grade\" function will be available for "
        # __temp += "generation. A higher grade will be of better quality items in the inventory. \n"
        # __temp += "\n"
        __temp += " \t \"random\" feachures for all catalogs especially for inventory.\n"
        __temp += "\n"
        __temp += "Error and exception handling \n"
        __temp += "\n"
        __temp += "Make more resources \n"

        print(__temp)
    else:
        print("UNCORRECT INPUT")
