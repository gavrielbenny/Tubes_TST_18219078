import json
from fastapi import FastAPI, HTTPException, Depends


with open("order.json", "r") as read_file:
    data = json.load(read_file)
with open("payment.json", "r") as read_file2:
    data2 = json.load(read_file2)


app = FastAPI()
@app.get('/')
def root():
    return{'Order':'Item'}

@app.get('/order/{item_id}')
async def read_order(item_id: int):
    for order_item in data['order']:
        if order_item['id'] == item_id:
            return order_item
    raise HTTPException(
        status_code=404, detail=f'Item not found'
        )

@app.post('/payment/{item_id}/{item_name}/{item_price}')
async def write_payment(name: str, price: int):
    item_id = len(data2['payment'])+1
    newdata = {'id': item_id, 'name' : name, 'price' : price}
    if(item_id > 1):
        data2['payment'].append(newdata)
        with open("payment.json", "w") as write_file2:
            json.dump(data2, write_file2)
        write_file2.close()
        return data2