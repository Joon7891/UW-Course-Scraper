from course import get_course

def main():
    print("Course Name:")
    code, num = input().split()
    course = get_course(code, num)

    if course is None:
        print("Course Not Found")
    else:
        print(course)
        
if __name__ == "__main__":
    main()