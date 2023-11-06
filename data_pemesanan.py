from fastapi import FastAPI, HTTPException
import json
from pydantic import BaseModel


class Pesanan(BaseModel):
	id: int
	name: str

json_filename="data_pemesanan.json"

with open(json_filename,"r") as read_file:
	data = json.load(read_file)

app = FastAPI()

@app.get('/pemesanan')
async def read_all_pemesanan():
	return data['pemesanan']


@app.get('/pemesanan/{pesanan_id}')
async def read_pemesanan(pesanan_id: int):
	for pemesanan_pesanan in data['pemesanan']:
		print(pemesanan_pesanan)
		if pemesanan_pesanan['id'] == pesanan_id:
			return pemesanan_pesanan
	raise HTTPException(
		status_code=404, detail=f'pemesanan not found'
	)

@app.post('/pemesanan')
async def add_pemesanan(pesanan: Pesanan):
	pesanan_dict = pesanan.dict()
	pesanan_found = False
	for pemesanan_pesanan in data['pemesanan']:
		if pemesanan_pesanan['id'] == pesanan_dict['id']:
			pesanan_found = True
			return "Pemesanan ID "+str(pesanan_dict['id'])+" exists."
	
	if not pesanan_found:
		data['pemesanan'].append(pesanan_dict)
		with open(json_filename,"w") as write_file:
			json.dump(data, write_file)

		return pesanan_dict
	raise HTTPException(
		status_code=404, detail=f'pesanan not found'
	)

@app.put('/pemesanan')
async def update_pemesanan(pesanan: Pesanan):
	pesanan_dict = pesanan.dict()
	pesanan_found = False
	for pemesanan_idx, pemesanan_pesanan in enumerate(data['pemesanan']):
		if pemesanan_pesanan['id'] == pesanan_dict['id']:
			pesanan_found = True
			data['pemesanan'][pemesanan_idx]=pesanan_dict
			
			with open(json_filename,"w") as write_file:
				json.dump(data, write_file)
			return "updated"
	
	if not pesanan_found:
		return "Pemesanan ID not found."
	raise HTTPException(
		status_code=404, detail=f'pesanan not found'
	)

@app.delete('/pemesanan/{pesanan_id}')
async def delete_pemesanan(pesanan_id: int):

	pesanan_found = False
	for pemesanan_idx, pemesanan_pesanan in enumerate(data['pemesanan']):
		if pemesanan_pesanan['id'] == pesanan_id:
			pesanan_found = True
			data['pemesanan'].pop(pemesanan_idx)
			
			with open(json_filename,"w") as write_file:
				json.dump(data, write_file)
			return "updated"
	
	if not pesanan_found:
		return "Pemesanan ID not found."
	raise HTTPException(
		status_code=404, detail=f'pesanan not found'
	)
