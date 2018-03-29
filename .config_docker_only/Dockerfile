# docker build -t ec2-deploy -f Dockerfile .

FROM        fc-youtube:base

# Dockerfile.base 이미지는 만든 후 수정을 거의하지 않기 때문에
# 아래 레이어는 만든 시점 이후에 변경된 코드들을 업데이트 하는 역할을 함.
COPY        . /srv/project

# Nginx 설정파일 복사 및 링크
RUN         cp -f /srv/project/.config/nginx/nginx.conf /etc/nginx/nginx.conf
RUN         cp -f /srv/project/.config/nginx/nginx-app.conf /etc/nginx/sites-available/
RUN         rm -f /etc/nginx/sites-enabled/*
RUN         ln -sf /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/

# supervisor 설정파일 복사
RUN         cp /srv/project/.config/supervisord.conf /etc/supervisor/conf.d/

# supervisor를 실행
CMD         pkill nginx; supervisord -n
           # -> CMD명령어는 Dockerfile에서 한번만 사용가능하기 때문에 동시에 작성.
