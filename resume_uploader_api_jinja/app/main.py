from fastapi import FastAPI, Request
from app.resume.routers import router as resume_router
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.db.config import SessionDep
from app.resume.services import get_all_resumes


app = FastAPI()


app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

templates = Jinja2Templates(directory="app/templates")

app.include_router(resume_router)


INDIAN_STATES=[
    "Andhra Pradesh", "Arunachal Pradesh","Assam", "Bihar", "Chattisgarh","Goa","Gujrat","Haryana","Himachal Pradesh"
    "Jharkhand","Karnataka","kerala","Madhya Pradesh","Maharashtra","Manipur","Mizoram","Odisha","Punjab",
    "Tripura","Uttar Pradesh","Uattarkhand","Rajsthan","Telangana","Ladakh","Delhi","Jammu & Kashmir","Nagaland" 
]

PREFERRED_LOCATIONS=[
    "Bangalore","Hydrabad","Mumbai","Delhi","Chennai","Pune","Kolkata","Ahamdabad","Jaipur"
]



@app.get("/", response_class=HTMLResponse)
async def resume_list(request: Request, session: SessionDep):
    resumes = await get_all_resumes(session)
    return templates.TemplateResponse("resume_list.html",{"request": request, "resumes": resumes})


@app.get("/create", response_class=HTMLResponse)
def form(request:Request):
    return templates.TemplateResponse("upload_resume.html",{
        "request": request,
        "indian_states": INDIAN_STATES,
        "preferred_location_options":PREFERRED_LOCATIONS
    })
