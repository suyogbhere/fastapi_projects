from fastapi import FastAPI, BackgroundTasks



app = FastAPI()


def write_notification(email: str, message: str = ""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)


    
@app.post("/send-notification/{email}")
async def send_notification(email: str, background_task: BackgroundTasks):
    background_task.add_task(write_notification, email, message= "Sent notification by geekshows")
    return {"message": "Notification sent !!!"}
