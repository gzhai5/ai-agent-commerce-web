# Data for the commerce website
# Since it is a quick demo, we will use in-memory data structures instead of a real database
# In a production system, you would replace this with actual database calls
from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    description: str
    category: str
    image_url: str = ""
    image_description: str = ""

products: list[Product] = [
    Product(
        id=1,
        name="LV Corduroy And Shearling Mix Trucker",
        description="This cozy shearling trucker jacket adds a luxurious twist to a casual silhouette for chic après-ski moments. The collar, yoke and sleeves are all crafted from soft shearling, while the body is assembled from thick-ribbed corduroy. Louis Vuitton savoir-faire informs the signature accents in iconic VVN-colored leather on the sleeve, back and leather zipper puller. Matching corduroy pants complete the look.",
        image_url="https://us.louisvuitton.com/images/is/image/lv/1/PP_VP_L/louis-vuitton-corduroy-and-shearling-mix-trucker--HUL13WCV9102_PM2_Front%20view.png?wid=2400&hei=2400",
        image_description="""
            a brown shearling-lined jacket with a classic, rugged design. It features a soft suede and corduroy exterior, combining two warm earthy textures. The collar and sleeve cuffs are lined with white shearling, adding both warmth and visual contrast.
            The jacket has a front zip closure with a leather zipper pull, two button-flap chest pockets, and clean seam detailing that enhances its structured silhouette. The overall aesthetic balances vintage workwear and modern luxury, offering a stylish and functional winter outerwear piece.""",
        category="Clothing"
    ),
    Product(
        id=2,
        name="LV Monogram Down Blouson",
        description="This cozy down blouson in an elegant dark brown is easy to mix and match with both winter sport and city looks. An allover tone-on-tone Monogram pattern adorns the technical jacquard fabric, while the flattering, enveloping silhouette is filled with Ecodown© for high-performance warmth. Damier and VVN-colored leather details recalling the House’s leather goods heritage lend a sophisticated finishing touch.",
        image_url="https://us.louisvuitton.com/images/is/image/lv/1/PP_VP_L/louis-vuitton-monogram-down-blouson--HUB07WQRS810_PM2_Front%20view.png?wid=2400&hei=2400",
        image_description="""
            a brown puffer jacket with a matte finish and subtle monogram pattern throughout the fabric. The jacket features a voluminous, quilted construction, offering excellent insulation and a structured silhouette.
            It includes a high padded hood with drawstrings tipped in gold hardware, a front snap-button closure, and side welt pockets with buttoned flaps for practicality. The cuffs and hem are elasticated, ensuring a snug fit to keep warmth in.
            Overall, it’s a luxury winter down jacket that blends classic puffer functionality with refined monogram detailing, projecting both comfort and sophistication.""",
        category="Clothing"
    ),
    Product(
        id=3,
        name="LV Flannel Shirt",
        description="This soft cotton flannel shirt is perfect for relaxed evenings by a roaring fire. It is adorned with a jacquard plaid in navy blue tones incorporating Damier elements. The collar and cuffs stand out in corduroy, while a VVN-colored leather signature patch and LV embroidery on the collar add smart finishing touches. This graphic piece can also be styled as an overshirt.",
        image_url="https://us.louisvuitton.com/images/is/image/lv/1/PP_VP_L/louis-vuitton-flannel-shirt--HUS01WE03653_PM2_Front%20view.png?wid=2400&hei=2400",
        image_description="""
            a navy blue button-up shirt featuring a geometric checkered pattern in varying shades of blue. The design alternates between solid and textured squares, creating a sophisticated grid-like visual effect reminiscent of a modern reinterpretation of a checkerboard motif.
            It has a dark contrasting collar—likely in a velvet or corduroy texture—and a button-down front closure. On the left chest area, there’s a small beige or tan leather patch embossed with a subtle emblem, adding a refined accent to the otherwise patterned shirt.
            Overall, this piece combines classic tailoring with a contemporary graphic twist, offering a polished yet casual look suitable for upscale or smart-casual wear.""",
        category="Clothing"
    ),
    Product(
        id=4,
        name="MIUMIU Cotton knit tank top",
        description="This soft cotton tank top combines simple lines and a contemporary character. Its versatile volumes adapt to bold layering, evoking new, sophisticated femininity. ",
        image_url="https://www.miumiu.com/content/dam/miumiubkg_products/M/MMV/MMV310/18HYF0009/MMV310_18HY_F0009_S_OOO_SLF.jpg/_jcr_content/renditions/cq5dam.web.hE7E3DA.2400.2400.jpg",
        image_description="""
            a minimalist white tank top with a clean and streamlined design. It features a sleeveless cut, a slightly squared neckline, and wide shoulder straps. The fabric appears to be soft and ribbed or finely textured, providing a comfortable and close fit.
            At the upper back, just below the neckline, there’s a small printed logo or text in black, adding a subtle design detail to an otherwise plain silhouette. The overall look is modern, versatile, and understated, suitable for layering or casual wear.""",
        category="Clothing"
    ),
    Product(
        id=5,
        name="MIUMIU Wool and leather zipper cardigan",
        description="This zip-up cardigan blends relaxed sportiness with an iconic design. The refined combination of fine knitwear and soft leather details lends the piece a distinctive character, expressing a modern, authentic femininity",
        image_url="https://www.miumiu.com/content/dam/miumiubkg_products/M/MMJ/MMJ150/177QF04V6/MMJ150_177Q_F04V6_S_OOO_SLF.jpg/_jcr_content/renditions/cq5dam.web.hE7E3DA.2400.2400.jpg",
        image_description="""
            a brown zip-up cardigan jacket that elegantly merges fine knitwear and soft suede leather. The front panel and collar are made from smooth suede, while the sleeves, hem, and cuffs are crafted from ribbed knit fabric, creating a refined contrast in texture.
            The jacket features a high ribbed collar, full front zipper, and discreet side pockets, offering both function and sophistication. A subtle embossed logo appears on the left chest, maintaining the minimalist and luxurious aesthetic.
            Overall, it exudes relaxed sportiness with timeless refinement, expressing a modern, authentic femininity through its balanced mix of comfort, craftsmanship, and elegant design.""",
        category="Clothing"
    ),
    Product(
        id=6,
        name="Balenciaga Men's Track Trail Laces Sneaker in White",
        description="""
            • Leather free
            • Sneaker
            • Polyurethane, polyester and polyamide
            • Written size at the edge of the toe
            • Track debossed at the back of the heel
            • BB debossed on front of the outsole
            • Printed logo on the exterior
            • Debossed logo on the tongue
            • Laces with cord lock at back
            • Double laces knotted in a usual equipment way
            • Back and tongue pull-on tab
            • Dynamic sole design with an augmented back for more comfort
            • Made in China
        """,
        image_url="https://balenciaga.dam.kering.com/asset/d336a28d-4b25-47ae-a18f-c7aa50850071/Large/800592WTRHK9110_F.jpg?v=1",
        image_description="""
            a white Balenciaga Track Sneaker, known for its layered, deconstructed design and technical, futuristic aesthetic.
            The shoe features a complex multi-panel construction combining mesh and synthetic overlays, delivering both breathability and structure. It has a chunky sole with dynamic sculpting, offering traction and a bold silhouette. The Balenciaga logo is printed on the outer side of the toe box, and dual laces—one in black and one in white—add visual contrast and utility-inspired flair.
            At the heel, a rubberized cage structure and pull tab enhance the sneaker’s sporty, trail-inspired look. Overall, it embodies high-performance design fused with avant-garde street style, a signature of Balenciaga’s contemporary sneaker lineup.""",
        category="Footwear",
    ),
    Product(
        id=7,
        name="Men's Gucci Re-Web sneaker",
        description="The Re-Web sees Gucci’s heritage stripes as a bold statement detail on a contemporary silhouette. Defined by signature details, this pair of sneakers is crafted from beige and blue Original GG canvas and completed with green and red Web tongue.",
        image_url="https://media.gucci.com/style/White_South_0_160_540x540/1689611500/760775_FACMZ_9746_002_100_0000_Light.jpg",
        image_description="""
            a pair of Gucci Ace sneakers, a classic low-top style featuring the brand’s iconic design elements.
            These sneakers are crafted from beige GG Supreme canvas, printed all over with the recognizable interlocking GG monogram pattern. Each side showcases the signature green and red web stripe, adding a touch of timeless Gucci identity. The heel tabs are finished in dark green leather, while the white rubber sole and white laces complete the clean, balanced silhouette.
            Overall, this pair exemplifies luxury streetwear elegance, blending vintage monogram heritage with modern casual sophistication.
        """,
        category="Footwear"
    ),
    Product(
        id=8,
        name="Prada Suede loafers",
        description="The classic loafer is reinterpreted with a light, tapered silhouette, enriched by the soft and sophisticated finish of suede. The refined artisan construction emphasizes the sleek, minimalist character of the design decorated with the lettering logo.",
        image_url="https://www.prada.com/content/dam/pradabkg_products/2/2DB/2DB229/103F0003/2DB229_103_F0003_F_X000_SLR.jpg/_jcr_content/renditions/cq5dam.web.hebebed.2400.2400.jpg",
        image_description="""
            a pair of brown suede loafers with a sleek, timeless silhouette. These shoes feature a soft, velvety suede upper with subtle hand-stitched detailing along the vamp, emphasizing craftsmanship and refinement.
            A small embossed logo is discreetly placed on the upper front, adding a touch of understated branding. The loafers are finished with a low stacked heel and a smooth leather sole, enhancing both comfort and elegance.
            Overall, the design combines classic Italian sophistication with modern minimalism, making these loafers ideal for both casual and smart-formal wear.
        """,
        category="Footwear"
    ),
    Product(
        id=9,
        name="Nike Air Jordan 1 Retro High OG",
        description="This iteration of the AJ1 reimagines Mike's first signature model with a fresh mix of colors. Premium materials, soft cushioning and a padded ankle collar offer total support and celebrate the shoe that started it all. Shown: Pale Ivory/Fir/Coconut Milk/Pro Green",
        image_url="https://static.nike.com/a/images/t_web_pdp_535_v2/f_auto,u_126ab356-44d8-4a06-89b4-fcdcc8df0245,c_scale,fl_relative,w_1.0,h_1.0,fl_layer_apply/7950b1e6-5a84-4843-94f6-68d741cbb463/WMNS+AIR+JORDAN+1+RETRO+HI+OG.png",
        image_description="""
            a Nike Air Jordan 1 High sneaker in a green and cream colorway. The shoe features a classic leather construction with dark green overlays and a cream base, giving it a refined yet sporty look.
            The Nike Swoosh is rendered in green leather, matching the toe box, eyestay, and heel panels, while the midsole maintains a vintage off-white tone. A gold Air Jordan Wings logo is embossed near the ankle collar, adding a touch of contrast and heritage flair.
            With its timeless silhouette and rich color balance, this sneaker blends retro basketball aesthetics with modern streetwear appeal.
        """,
        category="Footwear"
    ),
    Product(
        id=10,
        name="LV Trainer Sneaker Black",
        description="The iconic LV Trainer sneaker is revisited this season in a combination of Monogram denim and Monogram-embossed grained calf leather. The contrasting colors and materials highlight the elaborate construction of this model, which was inspired by vintage basketball sneakers.",
        image_url="https://us.louisvuitton.com/images/is/image/lv/1/PP_VP_L/louis-vuitton-lv-trainer-sneaker--BM9U5PMI02_PM2_Front%20view.png?wid=2400&hei=2400",
        image_description="""
            a pair of Louis Vuitton Trainer sneakers in a black and white colorway. These low-top sneakers feature a premium mix of materials, including smooth white leather and black Monogram denim overlays that highlight Louis Vuitton’s iconic pattern.
            The design incorporates LV branding on the tongue and side strap, along with embossed monogram details across the upper. The two-tone rubber sole showcases the brand’s signature Monogram flower motifs on the heel, adding a distinctive touch of luxury craftsmanship.
            With their bold silhouette and refined detailing, these sneakers combine high-fashion aesthetics with sport-inspired comfort, emblematic of Louis Vuitton’s contemporary street-luxury style.
        """,
        category="Footwear"
    ),
    Product(
        id=11,
        name="LV Speedy Soft 30",
        description="The Speedy Soft 30 is reimagined as part of the LV Ski collection in the House’s signature Monogram Eclipse canvas. The iconic style is adorned with an exclusive double chain and crinkled leather keybell, and also includes a signature padlock. This edition is sized to fit a tablet, as well as other daily essentials.",
        image_url="https://us.louisvuitton.com/images/is/image/lv/1/PP_VP_L/louis-vuitton-speedy-soft-30--M15102_PM2_Front%20view.png?wid=2400&hei=2400",
        image_description="""
            a Louis Vuitton Speedy Bandoulière bag in black Monogram Eclipse canvas. It features the brand’s signature LV monogram pattern embossed throughout, exuding a timeless yet contemporary luxury appeal.
            The bag includes dual black leather top handles and a detachable shoulder strap for versatile wear. A standout design element is the decorative gold and silver chain detail draped across the front—composed of mixed metallic links and stud-like charms—that adds an edgy, fashion-forward touch.
            Completing the design are silver-tone hardware, a black leather name tag, and a secure zip closure. The overall look blends classic Louis Vuitton craftsmanship with modern urban sophistication, making it both a statement piece and a practical everyday bag.
        """,
        category="Handbags"
    ),
    Product(
        id=12,
        name="LV Hobo MM Color Tan",
        description="Updated for the season in refined soft suede, this edition of the Hobo MM combines a 70s bohemian aesthetic with sleek LV lines. It is elevated with chocolate leather trims and a signature padlock in an aged gold-toned finish. Functional and chic, the versatile design includes an interior pocket and also features a removable Monogram pouch to store smaller items on the go.",
        image_url="https://us.louisvuitton.com/images/is/image/lv/1/PP_VP_L/louis-vuitton-hobo-mm--M25516_PM2_Front%20view.png?wid=2400&hei=2400",
        image_description="""
            a luxurious caramel-brown suede handbag with a minimalist triangular silhouette. It features a single structured top handle in dark leather, elegantly attached with gold-tone hardware, creating a sophisticated contrast.
            The surface of the bag is smooth and unadorned, except for a discreet embossed logo near the bottom center, emphasizing understated elegance. Its soft suede texture gives it a refined, tactile appeal, while the clean lines and sculptural form convey modern sophistication.
            Overall, this piece embodies timeless minimalism and quiet luxury, perfect for elevating both casual and formal ensembles.
        """,
        category="Handbags"
    ),
    Product(
        id=13,
        name="Balenciga Women's Le City Bag East-west in Black",
        description="""
            • Arena Storico lambskin
            • Two handles with one handle clip
            • Shoulder carry
            • Brass hardware
            • Zipped closure with knotted leather puller
            • Front zipped pocket with knotted leather puller
            • 1 main compartment
            • 1 inner flat pocket
            • Cotton canvas lining
            • Made in Italy
        """,
        image_url="https://balenciaga.dam.kering.com/m/52e7f958659fe0c1/Large-8457042ABEK1000_F.jpg?v=4",
        image_description="""
            a black Balenciaga Neo Classic City bag in a sleek, elongated silhouette. Crafted from shiny, crinkled leather, it captures Balenciaga’s signature edgy-luxury aesthetic.
            The bag features two rolled leather top handles, a front zip pocket with a distinctive leather pull tab, and aged metal studs and buckles that enhance its iconic rock-chic character. Side buckle details and long leather tassels add movement and attitude to the design.
            Compact yet structured, this piece embodies modern sophistication fused with vintage rebellion, making it a timeless statement accessory for both everyday and elevated looks.""",
        category="Handbags"
    ),
    Product(
        id=14,
        name="Celine MEDIUM AVA TRIOMPHE BAG IN smooth Calfskin",
        description="FIRST INTRODUCED IN THE WINTER 2023 COLLECTION, THE CELINE AVA TRIOMPHE BAG ESTABLISHES ITSELF AS A NEW CLASSIC FOR THE HOUSE. WORN ON THE SHOULDER, COMPLEMENTING THE HALF MOON SHAPE OF THE BAG, THE AVA IS AN ESSENTIAL TO THE CELINE SILHOUETTE, INCLUDING THE SIGNATURE TRIOMPHE ICONIC TO THE CELINE RENAISSANCE.",
        image_url="https://image.celine.com/2bd0676ac97b46f/original/114493DGQ-38NO_1_FW23_W.jpg?im=Resize=(1200);AspectCrop=(1,1),xPosition=.5,yPosition=.5",
        image_description="""
            a black Celine Ava Triomphe bag, a sleek and elegant shoulder bag characterized by its crescent-shaped silhouette. Crafted from smooth leather, it features the house’s signature Triomphe metal clasp in gold-tone hardware, positioned prominently on the front flap.
            The design includes a short adjustable shoulder strap with gold-tone attachments, allowing for versatile wear on the shoulder or arm. The minimal stitching and clean lines highlight Celine’s modern yet timeless aesthetic.
            This piece embodies refined Parisian sophistication, balancing minimalism with iconic branding—ideal for both everyday use and evening occasions.""",
        category="Handbags"
    ),
    Product(
        id=15,
        name="Dior Saddle Bag with Strap",
        description="Maria Grazia Chiuri brings a fresh update to the iconic Saddle bag. Crafted in blue Dior Oblique jacquard, the legendary design features a Saddle flap with a D stirrup clasp and magnetic pull, as well as an antique gold-finish metal CD signature on either side of the top handle. Equipped with a thin, adjustable and removable strap, the Saddle bag may be carried by hand, worn over the shoulder or crossbody.",
        image_url="https://assets.christiandior.com/is/image/diorprod/M0455CTZQM928_E01?$default_GHC$&crop=275,103,1320,1888&wid=1850&hei=2000&scale=0.875&bfc=on&qlt=85",
        image_description="""
            a Dior Saddle Bag, one of the brand’s most iconic designs. This version features the blue Dior Oblique jacquard canvas, paired with smooth navy leather trim that enhances its elegant, sculptural silhouette.
            The bag retains its signature asymmetric, saddle-inspired flap and distinctive “D” stirrup charm in antique gold-finish metal, which dangles from the front strap. The shoulder strap is crafted from leather and attaches with gold-tone hardware, giving the bag a refined equestrian feel.
            This piece perfectly blends heritage craftsmanship and contemporary luxury, embodying Dior’s timeless Parisian chic with a bold, statement-making design.""",
        category="Handbags"
    ),
]