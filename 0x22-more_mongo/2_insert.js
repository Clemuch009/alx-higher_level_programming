use products_db
db.products.insertMany([
  // Electronics
  { name: "Laptop Pro 15", category: "Electronics", price: 1199.99, stock: 15, description: "High-performance laptop with 15-inch display and 512GB SSD." },
  { name: "Wireless Earbuds", category: "Electronics", price: 79.99, stock: 60, description: "Noise-cancelling Bluetooth earbuds with charging case." },
  { name: "4K Smart TV", category: "Electronics", price: 899.99, stock: 8, description: "55-inch 4K UHD Smart TV with HDR and voice control." },
  { name: "Gaming Mouse", category: "Electronics", price: 49.99, stock: 120, description: "Ergonomic RGB mouse with adjustable DPI settings." },
  { name: "Smartwatch X", category: "Electronics", price: 199.99, stock: 30, description: "Fitness and heart rate tracking smartwatch." },

  // Furniture
  { name: "Office Chair Deluxe", category: "Furniture", price: 189.99, stock: 25, description: "Ergonomic mesh chair with adjustable armrests." },
  { name: "Wooden Dining Table", category: "Furniture", price: 499.99, stock: 10, description: "Solid oak dining table for six people." },
  { name: "Modern Sofa Set", category: "Furniture", price: 1299.99, stock: 5, description: "Three-piece sofa set with premium fabric." },
  { name: "Bookshelf Classic", category: "Furniture", price: 149.99, stock: 20, description: "Five-tier wooden bookshelf in walnut finish." },

  // Footwear
  { name: "Running Shoes", category: "Footwear", price: 99.99, stock: 40, description: "Lightweight running shoes for all terrains." },
  { name: "Leather Boots", category: "Footwear", price: 159.99, stock: 18, description: "Durable brown leather boots with anti-slip sole." },
  { name: "Flip Flops", category: "Footwear", price: 14.99, stock: 100, description: "Casual beach flip flops with foam cushioning." },

  // Clothing
  { name: "Men's Hoodie", category: "Clothing", price: 59.99, stock: 35, description: "Soft cotton hoodie with kangaroo pocket." },
  { name: "Women's Jeans", category: "Clothing", price: 69.99, stock: 50, description: "Slim-fit stretch denim jeans." },
  { name: "Baseball Cap", category: "Clothing", price: 24.99, stock: 75, description: "Adjustable cotton cap with embroidered logo." },
  { name: "Winter Jacket", category: "Clothing", price: 149.99, stock: 20, description: "Insulated waterproof winter jacket." },

  // Books
  { name: "The Art of Coding", category: "Books", price: 39.99, stock: 22, description: "A comprehensive guide to programming concepts." },
  { name: "AI Revolution", category: "Books", price: 29.99, stock: 30, description: "Exploring the impact of artificial intelligence." },
  { name: "Space Explorers", category: "Books", price: 34.99, stock: 18, description: "Stories from astronauts and space engineers." },

  // Kitchen
  { name: "Blender 9000", category: "Kitchen", price: 99.99, stock: 25, description: "High-speed blender with multiple blending modes." },
  { name: "Non-stick Pan Set", category: "Kitchen", price: 79.99, stock: 40, description: "3-piece non-stick frying pan set." },
  { name: "Electric Kettle", category: "Kitchen", price: 49.99, stock: 60, description: "1.7L stainless steel electric kettle." },
  { name: "Microwave Oven", category: "Kitchen", price: 229.99, stock: 15, description: "Compact digital microwave with grill feature." },
 {
    name: "ROS2 Development Kit",
    category: "Robotics",
    price: 89.99,
    stock: 12,
    description: "Complete kit for Robot Operating System 2, ideal for autonomous navigation prototypes."
  },
  {
    name: "Gripper Arm Assembly",
    category: "Robotics",
    price: 175.00,
    stock: 6,
    description: "Pneumatic gripper for industrial robotic manipulation tasks."
  },

  // Embedded Systems Additions
  {
    name: "Arduino Nano 33 BLE",
    category: "Embedded Systems",
    price: 29.99,
    stock: 75,
    description: "Compact BLE-enabled board for wireless embedded sensor networks."
  },
  {
    name: "ESP32-CAM Module",
    category: "Embedded Systems",
    price: 12.50,
    stock: 200,
    description: "Low-cost camera module for AI vision on edge devices."
  },

  // AI Additions
  {
    name: "TensorFlow Lite Kit",
    category: "AI",
    price: 45.99,
    stock: 40,
    description: "Hardware accelerator for lightweight ML models on microcontrollers."
  },
  {
    name: "Edge TPU Coral USB",
    category: "AI",
    price: 74.99,
    stock: 18,
    description: "Google's Coral for accelerating TensorFlow inferences in real-time."
  },

  // Aerospace Additions
  {
    name: "UAV Flight Controller",
    category: "Aerospace",
    price: 249.99,
    stock: 9,
    description: "Pixhawk-compatible controller for drone autopilot systems."
  },
  {
    name: "Avionics GPS Receiver",
    category: "Aerospace",
    price: 135.00,
    stock: 22,
    description: "High-precision GPS for satellite and aircraft navigation."
  },

  // Data Systems Additions
  {
    name: "InfluxDB Edge Node",
    category: "Data Systems",
    price: 99.99,
    stock: 35,
    description: "Time-series database node for distributed data logging."
  },
  {
    name: "Kafka Stream Processor",
    category: "Data Systems",
    price: 155.00,
    stock: 14,
    description: "Appliance for real-time stream processing in IoT data pipelines."
  }
])

