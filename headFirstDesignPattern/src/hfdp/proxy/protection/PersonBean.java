package hfdp.proxy.protection;

/**
 * @author Lwabish
 */
public interface PersonBean {

    /**
     * name getter
     *
     * @return name
     */
    String getName();

    /**
     * gender getter
     *
     * @return gender
     */
    String getGender();

    /**
     * interests getter
     *
     * @return interests
     */
    String getInterests();

    /**
     * rating getter
     *
     * @return rating
     */
    int getHotOrNotRating();

    /**
     * name setter
     *
     * @param name name
     */
    void setName(String name);

    /**
     * gender setter
     *
     * @param gender gender
     */
    void setGender(String gender);

    /**
     * interests setter
     *
     * @param interests interests
     */
    void setInterests(String interests);

    /**
     * rating setter
     *
     * @param rating rating
     */
    void setHotOrNotRating(int rating);
}
