import { useState, useEffect } from "react"
import ProductForm from "./Productform"


const ProductList = () => {
    const [products, setProducts] = useState([]);
    const fetchProducts = async () => {
        const res = await fetch('http://localhost:8000/products');
        const data = await res.json();
        setProducts(data);
    };

    return (
        <div>
            <ul>
                {products.map((p) => (
                    <li key={p.id}>
                        <strong>{p.title}</strong>: {p.description}
                    </li>
                ))}
            </ul>
        </div>

    )
}


export default ProductList