// task twelve - in stock
// create an express server
// do some redis
import redis from 'redis';
const redis = new Redis();
import express from 'express';
const app = express();
const port = 1245;

listProducts = [
  {Id: 1, name: 'Suitcase 250', price: 50, stock: 4},
  {Id: 2, name: 'Suitcase 450', price: 100, stock: 10},
  {Id: 3, name: 'Suitcase 650', price: 350, stock: 2},
  {Id: 4, name: 'Suitcase 1050', price: 550, stock: 5}
  ]

function getItemById(id){
  return listProducts.find((product) => product.Id === id);
}
// create route GET /list_products that will return
// list of every available product with json format
app.get('/list_products', (req, res) => {
  const ourProducts = listProducts.map((product) => {
    return {
      itemId: product.Id,
      itemName: product.name,
      price: product.price,
      initialAvailableQuantity: product.stock,
    };
  });

  res.json(ourProducts);
});

// use redis to set stock for key item.ITEM_ID
function reserveStockById(itemId, stock) {
  const key = `item.${itemId}`;
  redis.set(key, stock);
}

//  return the reserved stock for a specific item
async function getCurrentReservedStockById(itemId) {
  const key = `item.${itemId}`;
  const reservedStock = await redis.get(key);
  return parseInt(reservedStock) || 0;
}
