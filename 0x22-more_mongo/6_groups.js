db.products.aggregate([
  {
    $group: {
      _id: "$category",  // Group by category
      avgPrice: { $avg: "$price" },  // Average price
      totalStock: { $sum: "$stock" },  // Sum stock
      itemCount: { $sum: 1 }  // Count items
    }
  },
  {
    $sort: { avgPrice: -1 }  // Highest avg price first
  },
  {
    $project: {
      _id: 0,
      category: "$_id",
      avgPrice: { $round: ["$avgPrice", 2] },  // Round to 2 decimals
      totalStock: 1,
      itemCount: 1
    }
  }
]);
