
'use strict';

// print items on Html page
const updatePageData = async (outTag = 'app') => {
	const itemsList = await loadItems();
	console.log(itemsList);
	document.querySelector(outTag).innerHTML = itemsList.length === 0
		? `
			<div>
				&#x1f494; Sorry we have some problem &#x1f41b;<br/>
				Probably you have an empty list<br/>
				or maybe server is broke &#x1f61f;
			</div>
		`
		:
			'<ul>' +
				itemsList.map(
					(item) => 
					`
						<li>
							<button onclick="modifyItem(${item.id},'${item.nome}',${item.qta})">&#x270d;</button>
							${item.nome} ${item.qta}
							<button onclick="removeItem(${item.id})">&#x274c;</button>
						</li>
					`
				).join('') +
			'</ul>';
				
};

// CREATE new item and add them to itemsList
const addItem = async (nome="",qta=-1) => {
	const data = await fetch(`./api`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify( {
					"id": -1,
					"nome": nome,
					"qta": qta
				}
			)
		}
	)
		.then(res => res.json())
		.catch(e => console.error(e));
	updatePageData();
	
};

const loadItems =
	async () => await fetch('./api')
		.then(res => res.json())
		.catch(e => console.error(e));

// DELETE (remove) a selected item by index
const removeItem = async (id = -1) => {
	const data = await fetch(`./api/${id}`, {method: 'DELETE'})
		.then(res => res.json())
		.catch(e => console.error(e));
	updatePageData();
	
};

// UPDATE (modify) a selected item by index
const modifyItem = async (id = -1, oldName = '', oldqta="") => {
	let name = prompt (`give a new value for "${oldName}"`,oldName);
	let qta = prompt(`give a new value for "${oldqta}"`,oldqta).trim();
	
	const data = await fetch(`./api/`, {
		method: 'PUT',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify( {
				"id": id,
				"nome": name,
				"qta": qta
			}
		)
	}
	)
	.then(res => res.json())
	.catch(e => console.error(e));
	updatePageData();
	
};
