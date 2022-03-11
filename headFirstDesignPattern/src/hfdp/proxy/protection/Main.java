package hfdp.proxy.protection;

import java.lang.reflect.Proxy;

/**
 * @author Lwabish
 */
public class Main {
    public static void main(String[] args) {
        Main main = new Main();
        main.run();
    }

    private void run() {
        PersonBean p1 = new PersonBeanImpl("lwabish", "male", "singing jumping and basketball");
        PersonBean ownerProxy = getOwnerProxy(p1);
        PersonBean nonOwnerProxy = getNonOwnerProxy(p1);

        // owner类代理不能给自己评分，其他都可以
        ownerProxy.getName();
        ownerProxy.getHotOrNotRating();
        ownerProxy.setGender("female");
        try {
            ownerProxy.setHotOrNotRating(10);
        } catch (Exception e) {
            System.out.println("error:尝试改自己的分数");
        }

        // nonOwner类代理不允许改资料，仅允许评分
        nonOwnerProxy.setHotOrNotRating(12);
        nonOwnerProxy.getHotOrNotRating();
        nonOwnerProxy.getGender();
        try {
            nonOwnerProxy.setName("stupid");
        } catch (Exception e) {
            System.out.println("error:尝试篡改他人资料");
        }
    }

    PersonBean getOwnerProxy(PersonBean personBean) {
        return (PersonBean) Proxy.newProxyInstance(
                personBean.getClass().getClassLoader(),
                personBean.getClass().getInterfaces(),
                new OwnerInvocationHandler(personBean)
        );
    }

    PersonBean getNonOwnerProxy(PersonBean personBean) {
        return (PersonBean) Proxy.newProxyInstance(
                personBean.getClass().getClassLoader(),
                personBean.getClass().getInterfaces(),
                new NonOwnerInvocationHandler(personBean)
        );
    }
}
