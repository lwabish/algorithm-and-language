package hfdp.compound.factory;

import hfdp.compound.Quackable;
import hfdp.compound.adapter.Goose;
import hfdp.compound.adapter.GooseAdapter;

/**
 * @author Lwabish
 */
public class GooseDuckFactory extends AbstractGooseFactory{
    @Override
    public Quackable createGooseDuck() {
        return new GooseAdapter(new Goose());
    }
}
