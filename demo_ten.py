#import tensorflow as tf
# example of constant on tensorflow..

#x = tf.constant([1,2,3,4])
#y = tf.constant([6,7,8,9])
#result = tf.multiple(x,y)
#sess = tf.session()
#print(sess.run(result))
#_sess.close()


# example of variable on tensorflow..
#x = tf.constant(35, name='x')
#y = tf.Variable(x + 5, name='y')

#model = tf.global_variables_initializer()

#with tf.Session() as session:
#    session.run(model)
#    print(session.run(y))


#example of placeholder on tensorflow..

import tensorflow as tf

x = tf.placeholder("float", None)
y = x * 2

with tf.Session() as session:
    result = session.run(y, feed_dict={x: [1, 2, 3]})
    print(result)

