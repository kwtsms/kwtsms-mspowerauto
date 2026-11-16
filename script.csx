/*
FILE:      script.csx
CREATED:   2026-11-16 15:12 +03
TASK:      Power Automate certification
AUTHOR:    kwtSMS
WHAT:      Moves the kwtSMS API username and password from the connection (HTTP Basic header) into the JSON
           body the kwtSMS API expects, sends "test" as the string the API accepts, and names the connector in
           the User-Agent.
WHY:       The live test on 2026-11-16 returned ERR003 on every action: setproperty policies with
           @connectionParameters() did not put the credentials into the body. Basic auth plus a script is the
           pattern certified connectors use (Telstra SMS).
USAGE:     Uploaded with the connector (pac connector create/update --script-file script.csx). Runs for every
           operation listed in apiProperties.json scriptOperations.
DEPENDS:   apiDefinition.swagger.json securityDefinitions basic_auth; .NET Standard 2.0 namespaces only.
*/
public class Script : ScriptBase
{
    private const string UserAgent = "kwtsms-powerautomate/1.1.0";

    public override async Task<HttpResponseMessage> ExecuteAsync()
    {
        var request = this.Context.Request;

        // Credentials arrive as "Authorization: Basic base64(username:password)" from the connection.
        string username = "", password = "";
        var auth = request.Headers.Authorization;
        if (auth != null && string.Equals(auth.Scheme, "Basic", StringComparison.OrdinalIgnoreCase) && !string.IsNullOrEmpty(auth.Parameter))
        {
            var raw = Encoding.UTF8.GetString(Convert.FromBase64String(auth.Parameter));
            var sep = raw.IndexOf(':');
            if (sep >= 0)
            {
                username = raw.Substring(0, sep);
                password = raw.Substring(sep + 1);
            }
        }
        request.Headers.Authorization = null; // the kwtSMS API reads credentials from the body only

        var body = new JObject();
        if (request.Content != null)
        {
            var text = await request.Content.ReadAsStringAsync().ConfigureAwait(false);
            if (!string.IsNullOrWhiteSpace(text))
            {
                body = JObject.Parse(text);
            }
        }
        body["username"] = username;
        body["password"] = password;
        if (body["test"] != null)
        {
            body["test"] = body["test"].ToString(); // the API accepts "1", not the integer 1
        }

        request.Content = CreateJsonContent(body.ToString(Newtonsoft.Json.Formatting.None));
        request.Headers.Remove("User-Agent");
        request.Headers.TryAddWithoutValidation("User-Agent", UserAgent);

        return await this.Context.SendAsync(request, this.CancellationToken).ConfigureAwait(false);
    }
}
