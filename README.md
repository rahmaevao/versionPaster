# Version paster

В данном репозитории находится скрипт, который формирует header файл, в котором
прописана версия репозитория, адерсс которой указан в строке:

```
os.chdir(r...)
```

Если изменений с последнего коммита нет, то версию представлет из себя строку,
которую возвращает `git describe --always`.

Если изменения были, то скрипт даст предупреждение и в строку версии добавится
строка ` but not quite`.