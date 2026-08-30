import alchemy as al

if __name__ == "__main__":
    print(al.create_air())
    
    try :
        print(al.create_earth())
    except AttributeError as e:
        print(e)
