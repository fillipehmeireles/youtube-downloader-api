# Youtube Downloader API

Usage:
- Download song: http://localhost:5000/download-music   -> JSON: {'video-url':'url...'}
- Download video: http://localhost:5000/download-video   -> JSON: {'video-url':'url...'}

<code> Songs are converted to .mp3. </code>
<table>
    <thead>
        <th> Endpoint </th>
        <th> Methods </th>
        <th> Rule </th>
    </thead>
    <tbody>
        <tr>
            <td> downloadBlueprint.downloadMusic </td>
            <td> POST </td>
            <td> /download-music </td>
        </tr>
         <tr>
            <td> downloadBlueprint.downloadVideo  </td>
            <td> POST </td>
            <td> /download-video </td>
        </tr>
         <tr>
            <td> index.index </td>
            <td> GET </td>
            <td> / </td>
        </tr>
    </tbody>
</table>
