select A.order_number as 주문번호, date_format(A.order_date, '%Y-%m-%d') as 주문일자, IFNULL(B.customer_name, "(거래처없음)") as 거래처명
FROM Orders as A
left join (
	select customer_id, customer_name
	from Customers
) B
on A.customer_id = B.customer_id
order by A.order_number