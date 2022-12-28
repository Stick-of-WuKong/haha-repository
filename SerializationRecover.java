import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

import org.apache.commons.collections.Transformer;
import org.apache.commons.collections.keyvalue.TiedMapEntry;
import org.apache.commons.collections.map.LazyMap;
import org.apache.commons.collections.map.ReferenceMap;
import org.apache.commons.collections.set.AbstractSerializableSetDecorator;
import org.apache.commons.collections.set.ListOrderedSet;

import net.sf.json.AbstractJSON;
import net.sf.json.JSONArray;

import java.util.concurrent.CopyOnWriteArrayList;
import java.util.concurrent.CopyOnWriteArraySet;
import java.util.concurrent.ConcurrentSkipListMap;
import java.util.concurrent.ConcurrentSkipListSet;

public class SerializationRecover {
    public static void main(String[] args) {
        Map map1 = new ReferenceMap();
        Object key = new Object();
        map1.put(key, new CopyOnWriteArrayList());

        Map map2 = new ReferenceMap();
        map2.put(key, new CopyOnWriteArraySet<>());

        Map map3 = new ConcurrentSkipListMap();
        map3.put(key, new ConcurrentSkipListSet());

        Map map4 = new HashMap();
        map4.put(key, new HashSet<>());

        Map map5 = LazyMap.decorate(
                new HashMap(),
                new Transformer[] { new ConstantTransformer(Runtime.class),
                        new InvokerTransformer("getMethod",
                                new Class[] { String.class,
                                        Class[].class },
                                new Object[] { "touch",
                                        new String[] { "/tmp/success" } }) });

        Map map6 = new HashMap();
        map6.put("loadFactor", 0.75);
    }
}
