import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from model.Item import Item

webapp = FastAPI()

templates = Jinja2Templates (
	directory = 'templates',
	autoescape = False,
	auto_reload = True
)

webapp.mount(
	'/static',
	app = StaticFiles(directory = 'static'),
	name = 'static'
)
index  = [0]
itemsList = []

# start your main file
@webapp.get('/', response_class = HTMLResponse)
async def root(req: Request):
	return templates.TemplateResponse(
		# 'root.advance.html',
		'root.html',
		{
			'request': req,
			'title': 'ShoppingList',
		}
	)

@webapp.get('/id')
async def root():
	return max(index)
	
# [CREATE] :: POST Method - create (add) new item in your list and send a json message
# example (POST) ./api/apple -> append apple item in your itemsList
@webapp.post('/api')
async def create(item:Item):
	try:
		print(item)
		itemsList.append(item)
		item.setId(max(index))
		index.append(int(max(index)+1))
		return{
			'message': f'item added',
			'success': True
		}
	except Exception as e:
		print(e)
		return {
			'message': f'item not added',
			'success': False
		}


# [READ] :: GET Method - read items from your list with json response
# example (GET) ./api/ -> sort and show all items from your itemsList
@webapp.get('/api')
async def read():
	return itemsList

# [DELETE] :: DELETE Method - Delete a specific item form index and response with json message
# example (DELETE) ./api/3 -> remove item at index 3 in your itemsList
@webapp.delete('/api/{id}')
async def delete(id: int = -1):
	print(itemsList)
	for i in range(len(itemsList)):
		if itemsList[i].id == id:
			return {
					'message': f'{itemsList.pop(i)} was removed..',
					'success': True
			}
	return {
		'message': f'maybe {id} is not a valid index..',
		'success': False
	}


# [UPDATE] :: PUT Method - modify (update) a specific item form index and response with json message
# example (PUT) ./api/ -> change item 
@webapp.put('/api/')
async def update(item:Item):
	oldId=item.id
	for i in range(len(itemsList)):
		if itemsList[i].id == oldId:
			itemsList.pop(i)
			itemsList.append(item)
			return {
				'message': f'update value',
				'success': True
			}
	return {
		'message': f'{id} is not a valid index..',
		'success': False
	}

if __name__ == '__main__':
	uvicorn.run(
		'shopapp:webapp',
		host = '0.0.0.0',
		port = 80,
		reload = True,
		http = 'httptools'
	)
