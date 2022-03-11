package hfdp.proxy.protection;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;

/**
 * @author Lwabish
 */
public class OwnerInvocationHandler implements InvocationHandler {
    PersonBean person;

    public OwnerInvocationHandler(PersonBean person) {
        this.person = person;
    }

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Exception {
        if (Constants.RATING_SETTER_NAME.equals(method.getName())) {
            // 不允许自己调用自己的setHotOrNotRating方法改变评分，其他皆可
            throw new IllegalAccessException();
        }
        return method.invoke(person, args);
    }
}