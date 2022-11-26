from fastapi import FastAPI
from routers import users
import time
import datetime


app = FastAPI()
app.include_router(users.router, tags=['users'])


@app.middleware('http')
async def add_process_time_header(request, call_next):
	start_time = time.time()
	response = await call_next(request)
	process_time = time.time() - start_time
	response.headers['X-Process-Time'] = str(process_time)
	return response


@app.on_event('startup')
def startup_event():
	with open('server_time_log.log', 'a') as log:
		log.write(f'Application started at: {datetime.datetime.now()} \n')


@app.on_event('shutdown')
def shutdown_event():
	with open('server_time_log.log', 'a') as log:
		log.write(f'Application shut down at: {datetime.datetime.now()} \n')
