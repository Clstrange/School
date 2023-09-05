public class Main {
    public static void main(String[] args) throws Exception {
        Policy policy = Policy.getInstance("John", "1234");
        System.out.println(policy.getName());
        policy.setName("George");
        System.out.println(policy.getName());
        Policy policy2 = Policy.getInstance("jeffery", "0000");
        System.out.println(policy2.getName());
        policy.getDescription();
        policy.setPolicyId("0011");
        System.out.println(policy.getPolicyId());
    }
}
