cat-client
==========

python client for [CAT](https://github.com/dianping/cat)

### 探索CAT

* 往cat打了一个messageTree，服务器按文档的方式运行，怎么看不到python打的数据呢？是要等一小时么？还是文档里描述的只是demo的服务器运行方式？

        #! /usr/bin/env python
        # coding: utf-8

        import socket
        import struct

        host = 'localhost'
        port = 2280

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))

        msg = ''
        msg += "PT1\tdomain\thostName\tipAddress\tthreadGroupName\tthreadId\tthreadName\tmessageId\tparentMessageId\trootMessageId\tsessionToken\n"

        msg += "E2012-01-02 15:33:41.987\ttype\tname\t0\there is the data.\t\n"

        size = struct.pack('!i', len(msg))

        msg = size + msg

        s.sendall(msg)

* 要往cat打数据，格式是：

    “message length”(4字节) +
    "PT1\tdomain\thostName\tipAddress\tthreadGroupName\tthreadId\tthreadName\tmessageId\tparentMessageId\trootMessageId\tsessionToken\n" +
     "t2012-01-02 15:33:41.987\tURL\tReview\t\n" + //
		      "E2012-01-02 15:33:41.987\tURL\tPayload\t0\tip=127.0.0.1&ua=Mozilla 5.0...&refer=...&...\t\n" + //
		      "A2012-01-02 15:33:41.987\tService\tAuth\t0\t20000us\tuserId=1357&token=...\t\n" + //
		      "t2012-01-02 15:33:42.009\tCache\tfindReviewByPK\t\n" + //
		      "E2012-01-02 15:33:42.009\tCacheHost\thost-1\t0\tip=192.168.8.123\t\n" + //
		      "T2012-01-02 15:33:42.010\tCache\tfindReviewByPK\tMissing\t1000us\t2468\t\n" + //
		      "A2012-01-02 15:33:42.012\tDAL\tfindReviewByPK\t0\t5000us\tselect title,content from Review where id = ?\t\n" + //
		      "E2012-01-02 15:33:42.027\tURL\tView\t0\tview=HTML\t\n" + //
		      "T2012-01-02 15:33:42.087\tURL\tReview\t0\t100000us\t/review/2468\t\n"
吗？就是一个messageTree的头+Transaction的序列化吗？

* 对于跨越两台机器的Transaction，cat是怎么表示的？比如一个RPC调用，在客户端记录client send和client recv两个时间点，而在服务器端记录server recv和server send，从Transaction的序列化看，Transaction并没有Id，那么两台机器的Transaction怎么联系起来呢？

* 对于不同机器发来的，messageID相同的两个messageTree，cat是怎么处理的？

* 如果一台机器A发出了一个messageTree(messageID=1, parentMessageID=None)，另一台机器B发出MessageTree(messageID=2, parentMessageID=1)，那么B发出的messageTree会不会被合并到A的messageTree里？

* ForkedTransaction和普通Transaction的区别是什么？用途是什么？
* messageTree里MessageId的格式一定要是域名-IP-...么？换成随机数会怎么样？
* 对于不同机器发来的，messageID相同的两个messageTree，cat是怎么处理的？
* 如果一台机器A发出了一个messageTree(messageID=1, parentMessageID=None)，另一台机器B发出MessageTree(messageID=2, parentMessageID=1)，那么B发出的messageTree会不会被合并到A的messageTree里？
* 如果每个rpc调用都是一个messageTree，都会flush，开销不会大么？即使用了queue作异步。
* ForkedTransaction和普通Transaction的区别是什么？用途是什么？
* 要登录，是要手动向数据库插入条目么？
