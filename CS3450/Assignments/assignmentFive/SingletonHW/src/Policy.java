public class Policy {
    String name;
    String policyId;
    private volatile static Policy uniquePolicy;
    private Policy(String name, String policyId){
        this.name = name;
        this.policyId = policyId;
    }

    public static Policy getInstance(String name, String policyId) {
        if (uniquePolicy == null) {

            synchronized (Policy.class) {
                if (uniquePolicy == null) {
                    uniquePolicy = new Policy(name, policyId);
                }
            }
        }
        return uniquePolicy;
    }

    public void getDescription() {
        System.out.println("This is the description of your policy");
    }
    public String getName() {
        return this.name;
    }

    public String getPolicyId() {
        return this.policyId;
    }

    public void setName(String newName) {
        this.name = newName;
    }

    public void setPolicyId(String newPolicyId) {
        this.policyId = newPolicyId;
    }
}
