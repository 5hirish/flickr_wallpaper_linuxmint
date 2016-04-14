# Flickr Wallpapers
This scrips daily fetchs 5 interesting pictures from 2 days ago from Flickr. It selects a random photo from those five photos and sets it as desktop wallpaper.
The setting Desktop Wallpaper feature supports only for Linux Mint 17.X. and Ubuntu.

**API Key required** Get it here: [Flickr App Garden](https://www.flickr.com/services/apps/create/)

### Flickr API method:
`flickr.interestingness.getList`
#### Arguments:
`api_key` (Required) : Your API application key. See here for more details.

`date` (Optional) : A specific date, formatted as YYYY-MM-DD, to return interesting photos for.

`extras` (Optional) : A comma-delimited list of extra information to fetch for each returned record. Currently supported fields are: description, license, date_upload, date_taken, owner_name, icon_server, original_format, last_update, geo, tags, machine_tags, o_dims, views, media, path_alias, url_sq, url_t, url_s, url_q, url_m, url_n, url_z, url_c, url_l, url_o

`per_page` (Optional) : Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.

`page` (Optional) : The page of results to return. If this argument is omitted, it defaults to 1.
#### Example:
`https://api.flickr.com/services/rest/?method=flickr.interestingness.getList&date=2016-04-11&per_page=5&api_key=YOUR_API_KEY`

#### Response:
Check the sample.xml file for Sample XML response.

#### Mapping to Photo URL

`https://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}_[mstzb].jpg`

For more info [Photo Source URLs](https://www.flickr.com/services/api/misc.urls.html)

#### Setting Wallpaper
Once the image is downloaded its stored in your home directory in *Pictures/Flickr*
Linux Mint 17.X users with Cinnamon DE supporting Gnome 3.XX can set wallpapers using:

`gsettings set org.cinnamon.desktop.background picture-uri  file:////absolute_path_of_image_no_spaces`

For Ubuntu Unity Users:

`gsettings set org.gnome.desktop.background picture-uri file:////absolute_path_of_image_no_spaces`
