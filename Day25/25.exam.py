
# < Network >
"""
 < TCP/IP Model >

상위계층. Application                           //  5장비. Pc, 서버 ..

4계층. Transport - TCP(쌍방) / UDP(일방)        //  4장비. L4 Sw
- 데이터 전송을 담당.              
- 신뢰성 있게 보내려면 TCP 방식 (응답을 준다.)으로
- 속도가 중요하면 UDP 방식으로 4계층 형성 (PORT 주소에 따라 결정)

3계층. Internet(Network)                        //  3장비. Router, L3 Sw      ex) 공유기  
- IP (src(출발지) -> dest(목적지))     

2계층. Network Interface                        //  2장비. Bridge, Switch
- Frame:  HEADER | Packet | TRAILER
  1) MAC(Media Access Control) address : ARP를 통해 알아낼 수 있음
  2) LLC(Logical Link Control)

1계층. Hardware(Physical) : Bit, Conn           //  1장비. Hub, Repeater
- 인코딩 하는 작업




< Data encapsulation & de-encapsulation >

4계층 Transport (TCP/UDP)
- TCP Segment (큰 데이터 쪼개서 보내는 개념) -> 네트워크 MTU에 따라 크기에 맞춰 쪼개짐
- Segment 나오면 4계층으로 이해하면 됨

3계층 Internet (IP)




< LAN Connections >
- 통신: 1,2(송신) 3,6(수신)

T568A (녹 주 청 갈)
T568B (주 녹 청 갈)
- 줄무니 단색 줄무니 단색... (반복)

1) Straight-Through Cable
- 다이렉트로 연결 (lan 구성 동일)
- 서로 다른 계층이 연결될 때 사용

2) Crossover Cable
- 같은 레벨의 단계의 계층 연결될 때 사용




< Internet Layer (3계층) >

Network (3계층)
- ICMP
- IP Address


IPv4, IPv6
1. IPv4: 32bit 
- ________ ________ ________ ________ 32bit (2^32)

- 클래스 종류

(맨 앞이 0일 때 나올 수 있는 모든 경우의 수)
1) A 클래스 
- 넷마스크(network mask): 255.0.0.0
- 사설IP: 10.0.0.0 ~ 10.255.255.255 (외부 통신이 불가능함!)
- loopback: 127.0.0.0 ~ 127.255.255.255 (127로 시작하는 IP는 나 자신을 의미 = 파이썬 self와 비슷한 개념)
ex)
00000000 00000000 00000000 00000000 => 0.0.0.0 (Net ID(0)/ Host ID(0.0.0))
01111111 11111111 11111111 11111111 => 127.255.255.255 (Net ID(127) / Host ID(.255.255.255))

-------------------------------------------------------------------------------------------

(맨 앞이 1일 때 나올 수 있는 모든 경우의 수)

2) B 클래스
- 넷마스크(network mask): 255.255.0.0
- 사설IP: 172.16.0.0 ~ 172.31.255.255
- DHCP할당실패: 169.254.0.0 ~ 169.254.255.255
ex)
10000000 00000000 00000000 00000000 => 128.0.0.0
10111111 11111111 11111111 11111111 => 191.255.255.255

3) C 클래스
- 넷마스크(network mask): 255.255.255.0
- 사설IP: 192.168.0.0 ~ 192.168.255.255
ex)
11000000 00000000 00000000 00000000 => 192.0.0.0
11011111 11111111 11111111 11111111 => 223.255.255.255

4) D 클래스
- 멀티캐스트 용도로 사용
ex)
11100000 00000000 00000000 00000000 => 224.0.0.0
11101111 11111111 11111111 11111111 => 239.255.255.255

5) E 클래스
ex)
11110000 00000000 00000000 00000000 => 240.0.0.0
11111111 11111111 11111111 11111111 => 255.255.255.255

실습) cmd -> ipconfig -> IPv4 주소확인
내 노트북 IPv4 주소: 192.168.0.46
==> 11000000.10101000.00000000.00101110 (Bit로 표현)


2. IPv6: 128bit
- ________ ________ ... 128bit (2^128)




< Type of Data Transmissions >

1) Unicast (유니캐스트)
- 1:1 로 송신
- A Host가 B Host에게 Data를 전달하는 가장 일반적인 방법.

2) Broadcast (브로드캐스트)
- 단일 Host가 Segment에 모든 호스트를 대상으로 Data를 전달 시 사용됨.
- 동일한 정보를 한번에 모든 호스트에게 전달하는 장점이 있음
- 많은 Broadcast는 호스트의 성능저하를 가져옴.
- 모든 애들(모든 IP)이 처리하도록   ex) 주소 = 255.255.255.255
- 2계층 MAC 은 올F 로 표기됨.

3) Multicast (멀티캐스트)
- 특정 그룹에게만 보내기 위한 방식




< 서브넷팅 >
ex)
192.168.100.0 / 24 을 서브넷팅 하면 (마스크 24(1이 24개) = 255.255.255.0)
11000000.10101000.01100100.00000000 (192.168.100.0) 0 ~
11000000.10101000.01100100.11111111 (192.168.100.0) 255


11111111.11111111.11111111.S0000000 마스크(S=1)를 기준으로 (서브넷 마스크)

11000000.10101000.01100100.00000000 0 ~
11111111.11111111.11111111.01111111 127

11000000.10101000.01100100.10000000 128 ~
11111111.11111111.11111111.11111111 255

두 덩이로 나눌 수 있다(0 ~ 127 / 128 ~ 255)

"""



