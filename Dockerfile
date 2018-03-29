FROM        smallbee3/fc-youtube:base
MAINTAINER  smallbee3@gmail.com

ENV         BUILD_MODE              production
ENV         DJANGO_SETTINGS_MODULE  config.settings.${BUILD_MODE}

# 소스폴더를 통째로 복사
COPY        . /srv/project

# nginx설정파일을 복사 및 링크
RUN         cp -f   /srv/project/.config/${BUILD_MODE}/nginx.conf       /etc/nginx/nginx.conf &&\
            cp -f   /srv/project/.config/${BUILD_MODE}/nginx-app.conf   /etc/nginx/sites-available/ &&\
            rm -f   /etc/nginx/sites-enabled/* &&\
            ln -sf  /etc/nginx/sites-available/nginx-app.conf   /etc/nginx/sites-enabled/


# supervisor설정파일을 복사
RUN         cp -f   /srv/project/.config/production/supervisord.conf /etc/supervisor/conf.d/




# 밑 과정 작업하다가 중지
# 빌드 과정에서하는게 별로 의미가 없기 때문에 뺀것
# 배포 과정에서 migrate, collecstatic 하는게 의미기 안맞음?
## 3/12 docker env googling
#ENV         PATH /srv/project/app/config/settings/production:$PATH
#
## Sqlite DB migrate, createsuperuser
#WORKDIR     /srv/project/app
#RUN         python manage.py migrate && python manage.py createsu




# pkill nginx후 supervisord -n실행
CMD         pkill nginx; supervisord -n



# EB에서 (nginx) 프록시로 연결될 Port를 열어줌
EXPOSE      80