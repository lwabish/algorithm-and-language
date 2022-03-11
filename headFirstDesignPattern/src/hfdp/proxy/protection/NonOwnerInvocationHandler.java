package hfdp.proxy.protection;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;

/**
 * @author Lwabish
 */
public class NonOwnerInvocationHandler implements InvocationHandler {

    PersonBean person;

    public NonOwnerInvocationHandler(PersonBean person) {
        this.person = person;
    }


    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Exception {
        // 仅允许改变别人的评分，其他不可
        if ("setHotOrNotRating".equals(method.getName())) {
            return method.invoke(person, args);
        } else if (method.getName().startsWith("set")) {
            throw new IllegalAccessException();
        } else if (method.getName().startsWith("get")) {
            return method.invoke(person, args);
        }
        return null;
    }
}
