public class University {
    private String name;
    public University (String name) {
        this.name = name;
    }

    class Student {
        private String studentName;

        public Student(String studentName) {
            this.studentName = studentName;
        }

        public void displayStudentInfo() {
            System.out.println("University: " + name);
            System.out.println("Student Name: " + studentName);
        }
    }
}
