<h1>zarinpal-payment</h1>

# how it work

<h4>simple setup for create order</h4>
<ul>
    <li>[MainPageView] - send selected item to url(for one item)</li>
    <li>[payment:main_page] - for [MainPageView]</li>
    <li>[BuyObjectView]
        <ul>
            <li>get item_id from url</li>
            <li>create object to save order information in database</li>
            <li>send user to zarinpal</li>
            <li>need authentication permission</li>
        </ul>
    </li>
    <li>[payment:buy_object] - for [BuyObjectView]</li>
</ul>
<br>
<h4>zarinpan steps</h4>
<ul>
    <li>[MainPageView] - send selected item to url(for one item)</li>
    <li>[payment:main_page] - for [MainPageView]</li>
    <li>[BuyObjectView]
        <ul>
            <li>get item_id from url</li>
            <li>create object to save order information in database</li>
            <li>send user to zarinpal</li>
            <li>need authentication permission</li>
        </ul>
    </li>
    <li>[payment:buy_object] - for [BuyObjectView]</li>
</ul>