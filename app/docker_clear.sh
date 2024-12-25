echo "Почистим почистим!"
for i in $(docker images -aq); do docker rmi -f $i; done
docker system prune -a
echo "Очищено!"

