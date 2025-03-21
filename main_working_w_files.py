from fastapi import FastAPI, UploadFile
from fastapi.responses import StreamingResponse, FileResponse

app = FastAPI()


# запись файла
@app.post("/files")
async def upload_file(uploaded_file: UploadFile):
    file = uploaded_file.file
    filename = uploaded_file.filename
    with open(f"1_{filename}", "wb") as f:
        f.write(file.read())  # записываем файл


@app.post("/multiple_files")
async def upload_files(uploaded_files: list[UploadFile]):  # принимает список файлов, который мы должны загрузить
    for uploaded_file in uploaded_files:  # порходим по всем файлам циклом
        file = uploaded_file.file
        filename = uploaded_file.filename
        with open(f"1_{filename}", "wb") as f:
            f.write(file.read())  # записываем файл


# Чтение локального файла
@app.get("/files/{filename}")
async def get_file(filename: str):
    return FileResponse(filename)


def iterfile(filename: str):
    with open(filename, "rb") as f:
        while chunk := f.read(1024 * 1024):  # считываем кусочек видео и нзываем его чанк
            yield chunk  # тут же этот чанк вернем


# Чтение  файла из облачного хранилища, удаленно (тут нужен генератор)
@app.get("/files/streaming/{filename}")
async def get_file_streaming(filename: str):
    return StreamingResponse(iterfile(filename), media_type="video/mp4")
