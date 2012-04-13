package us.jubat.classifier;

import org.junit.Before;
import org.junit.Test;

public class ClassifierTest {
	@Before
	public void setUp() throws Exception {
		// super.setUp();
	}

	public void tearDown() throws Exception {
		// super.tearDown();
	}

	@Test(expected = Exception.class)
	public void testHello() throws Exception {
		ClassifierClient c = new ClassifierClient("localhost", 9199, 10);

		// c.set_config("");
		c.get_config("");
		// / System.out.println("hello");
	}

	@Test
	public void testHello2() {
	}
}
