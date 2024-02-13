# Happy Lunar New Year! 🧧

Đầu xuân năm mới, mình xin chúc tất cả các bạn thành viên của VinUni Hacking Club sẽ có một năm mới thật nhiều năng lượng, nhiều sức khoẻ. Chúc mọi người và gia đình năm mới an khang thịnh vượng, vạn sự như ý. Chúc club của chúng ta sẽ có được nhiều thành công hơn nữa trong năm mới! 

## CTF! AES_ConBòCon 

Để mở đầu năm mới, cũng như một cơ hội để mọi người khai code đầu xuân, mình xin giới thiệu một bài CTF nhỏ: AES_ConBòCon.

### Build 

#### Dependencies

Để build được challenge này, các bạn cần cài đặt [Docker](https://www.docker.com/). Các bạn có thể lựa chọn Docker Engine hoặc Docker Desktop tùy theo hệ điều hành của mình.

1. Clone repository này về máy của bạn.

```bash
git clone https://github.com/h114mx001/aes_conbocon
```

1. Build Docker image

```bash 
cd aes_conbocon
echo "flag{this_is_a_fake_flag}" > milk
docker build -t aes_conbocon .
```

3. Run Docker container

```bash
docker run -d -p 31339:31339 aes_conbocon:latest
```

4. Kết nối tới server

```bash
nc 127.0.0.1 31339
```

5. Enjoy!!!

### Challenge

Access at: 

```bash
nc 103.82.24.40 31339
```