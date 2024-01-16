/* 
 * Selling Partner API for Solicitations
 *
 * With the Solicitations API you can build applications that send non-critical solicitations to buyers. You can get a list of solicitation types that are available for an order that you specify, then call an operation that sends a solicitation to the buyer for that order. Buyers cannot respond to solicitations sent by this API, and these solicitations do not appear in the Messaging section of Seller Central or in the recipient's Message Center. The Solicitations API returns responses that are formed according to the <a href=https://tools.ietf.org/html/draft-kelly-json-hal-08>JSON Hypertext Application Language</a> (HAL) standard.
 *
 * OpenAPI spec version: v1
 * 
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using SwaggerDateConverter = SpApiCsharpApp.swaggerClient.Client.SwaggerDateConverter;

namespace SpApiCsharpApp.swaggerClient.Model.Solicitations
{
    /// <summary>
    /// The response schema for the getSolicitationActionsForOrder operation.
    /// </summary>
    [DataContract]
    public partial class GetSolicitationActionsForOrderResponse :  IEquatable<GetSolicitationActionsForOrderResponse>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="GetSolicitationActionsForOrderResponse" /> class.
        /// </summary>
        /// <param name="links">links.</param>
        /// <param name="embedded">embedded.</param>
        /// <param name="errors">errors.</param>
        public GetSolicitationActionsForOrderResponse(GetSolicitationActionsForOrderResponseLinks links = default(GetSolicitationActionsForOrderResponseLinks), GetSolicitationActionsForOrderResponseEmbedded embedded = default(GetSolicitationActionsForOrderResponseEmbedded), ErrorList errors = default(ErrorList))
        {
            this.Links = links;
            this.Embedded = embedded;
            this.Errors = errors;
        }
        
        /// <summary>
        /// Gets or Sets Links
        /// </summary>
        [DataMember(Name="_links", EmitDefaultValue=false)]
        public GetSolicitationActionsForOrderResponseLinks Links { get; set; }

        /// <summary>
        /// Gets or Sets Embedded
        /// </summary>
        [DataMember(Name="_embedded", EmitDefaultValue=false)]
        public GetSolicitationActionsForOrderResponseEmbedded Embedded { get; set; }

        /// <summary>
        /// Gets or Sets Errors
        /// </summary>
        [DataMember(Name="errors", EmitDefaultValue=false)]
        public ErrorList Errors { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class GetSolicitationActionsForOrderResponse {\n");
            sb.Append("  Links: ").Append(Links).Append("\n");
            sb.Append("  Embedded: ").Append(Embedded).Append("\n");
            sb.Append("  Errors: ").Append(Errors).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as GetSolicitationActionsForOrderResponse);
        }

        /// <summary>
        /// Returns true if GetSolicitationActionsForOrderResponse instances are equal
        /// </summary>
        /// <param name="input">Instance of GetSolicitationActionsForOrderResponse to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(GetSolicitationActionsForOrderResponse input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Links == input.Links ||
                    (this.Links != null &&
                    this.Links.Equals(input.Links))
                ) && 
                (
                    this.Embedded == input.Embedded ||
                    (this.Embedded != null &&
                    this.Embedded.Equals(input.Embedded))
                ) && 
                (
                    this.Errors == input.Errors ||
                    (this.Errors != null &&
                    this.Errors.Equals(input.Errors))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.Links != null)
                    hashCode = hashCode * 59 + this.Links.GetHashCode();
                if (this.Embedded != null)
                    hashCode = hashCode * 59 + this.Embedded.GetHashCode();
                if (this.Errors != null)
                    hashCode = hashCode * 59 + this.Errors.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}